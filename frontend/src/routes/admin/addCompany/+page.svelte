<script lang="ts">
    import CompanyForm from "$lib/components/CompanyForm.svelte";
    import { fetcher } from "$lib/fetcher";
    import { toast } from "svelte-sonner";

    async function create(data: any) {
        const res = await fetcher("/api/admin/company", {
            method: "POST",
            body: JSON.stringify(data)
        })

        if (res.ok) {
            toast.success("Dodano nową firmę")
            return
        } 
        
        toast.error(`Błąd podczas dodawania firmy - ${res.status}`)
    }
</script>
<CompanyForm onSubmit={create} />

