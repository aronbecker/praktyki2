<script lang="ts">
    import CompanyCard from "$lib/components/CompanyCard.svelte";
    import FilterAndSortBar from "$lib/components/FilterAndSortBar.svelte";
    import SearchBar from "$lib/components/SearchBar.svelte"; 

    let { data } = $props();
    let companies = data.companies

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