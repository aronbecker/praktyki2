<script>
    import { getCompanies } from "$lib/companies.js";
    import CompaniesTable from "$lib/components/companiesTable.svelte";
    import Button from "$lib/components/ui/button/button.svelte";

    let { data } = $props()

    let currentPage = $state(0)
    let companies = $state(data.page.companies)

    async function loadMoreCompanies() {
        currentPage += 1
        const newPage = await getCompanies(currentPage)
        companies = [...companies, ...newPage.companies]
    }
</script>
<div class="overflow-auto mx-auto mb-auto">
    <CompaniesTable {companies} />
    {#if data.page.pages - 1 != currentPage}
        <div class="w-max mx-auto">
            <Button onclick={loadMoreCompanies}>Załaduj więcej</Button>
        </div>    
    {/if}
</div>
