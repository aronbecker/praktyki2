<script lang="ts">
    import { getCompanies } from "$lib/companies";
    import CompanyCard from "$lib/components/CompanyCard.svelte";
    import FilterAndSortBar from "$lib/components/FilterAndSortBar.svelte";
    import SearchBar from "$lib/components/SearchBar.svelte"; 
    import Button from "$lib/components/ui/button/button.svelte";

    let { data } = $props();
    let companies = $state(data.page.companies)
    let currentPage = $state(0)
    let page = $state(data.page)
    let rating = $state(-1)
    let category: string | null = $state(null)
    let text: string | null = $state(null)

    async function loadMoreCompanies(rating: number, category: string | null, search: string | null = null) {
        currentPage += 1
        page = await getCompanies(currentPage, rating, category, search)
        companies = [...companies, ...page.companies]
    }

    async function onSearch(text_: string) {
        text = text_ == "" ? null : text_
        currentPage = -1
        companies = []
        await loadMoreCompanies(rating, category, text)
    }

    async function onFilterSortChange(category_: string, rating_: string) {
        rating = 0
        category = null
        currentPage = -1
        companies = []

        if (!isNaN(rating_)) {
            rating = Number(rating_)
        } 
        
        if (category_ != "Wszystkie kategorie") {
            category = category_
        }

        await loadMoreCompanies(rating, category, text)
    }
</script>

<div class="column pt-4 pb-18 from-[#1F4067] to-[#1F4067/10] bg-linear-to-r">
    <h1 class="font-bold text-5xl text-center">Wyszukiwarka firm w <span class="text-primary">skokach</span></h1>
    <p class="text-muted-foreground text-center mx-4 mt-6 mb-8">Szybkim sposobem wyszukaj firmy, które fachowo wykonują zadania</p>
    <SearchBar onSearch={onSearch} />
</div>
<div class="row justify-center max-w-[1200px] w-[90%] mx-auto my-10 gap-8 flex-wrap">
    <FilterAndSortBar onChange={onFilterSortChange} />
    <div class="flex justify-center w-full mx-auto gap-8 flex-wrap">
        {#each companies as company}
            <CompanyCard {company}/>
        {/each}
    </div>
</div>
{#if page.pages - 1 > currentPage}
    <div class="w-max mx-auto">
        <Button onclick={loadMoreCompanies}>Załaduj więcej</Button>
    </div>    
{/if}