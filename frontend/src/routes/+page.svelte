<script lang="ts">
    import { getCompanies } from "$lib/companies";
    import CompanyCard from "$lib/components/CompanyCard.svelte";
    import FilterAndSortBar from "$lib/components/FilterAndSortBar.svelte";
    import SearchBar from "$lib/components/SearchBar.svelte"; 
    import Button from "$lib/components/ui/button/button.svelte";

    let { data } = $props();
    let companies = $state(data.page.companies)
    let currentPage = $state(0)

    async function loadMoreCompanies() {
        currentPage += 1
        const newPage = await getCompanies(currentPage)
        companies = [...companies, ...newPage.companies]
    }

    function onSearch(text: String) {
        alert("Wyszukiwanie " + text)
    }

    function onFilterSortChange(category: String, rating: String) {
        alert("Filtrowanie/Sortowanie zmienione")
    }
</script>

<div class="column pt-4 pb-18 from-[#1F4067] to-[#1F4067/10] bg-linear-to-r">
    <h1 class="font-bold text-5xl text-center">Wyszukiwarka firm w <span class="text-primary">skokach</span></h1>
    <p class="text-muted-foreground text-center mx-4 mt-6 mb-8">Szybkim sposobem wyszukaj firmy, które fachowo wykonują zadania</p>
    <SearchBar onSearch={onSearch} />
</div>
<div class="row justify-center max-w-[1200px] w-[90%] mx-auto my-10 gap-8 flex-wrap">
    <FilterAndSortBar onChange={onFilterSortChange} />
    {#each companies as company}
        <CompanyCard {company}/>
    {/each}
</div>
{#if data.page.pages - 1 != currentPage}
    <div class="w-max mx-auto">
        <Button onclick={loadMoreCompanies}>Załaduj więcej</Button>
    </div>    
{/if}