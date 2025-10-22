<script lang="ts">
    import CompanyForm from "$lib/components/CompanyForm.svelte";
    import { dialogStore, setDialog } from "$lib/stores/dialogStore";
    import * as Dialog from "$lib/components/ui/dialog/index.js";
    import { fetcher } from "$lib/fetcher";
    import { toast } from "svelte-sonner";

    let companyData = $state<string[]>([])
    dialogStore.subscribe(store => {
        // @ts-ignore
        companyData = store.data?.companyData
    })

    async function edit(data: any) {
        const res = await fetcher(`/api/admin/company/${companyData[0]}`, {
            method: "PATCH",
            body: JSON.stringify(data)
        })

        if (res.ok) {
            dialogStore.set({code: 0, data: {}})
            toast.success("Pomyślnie zapisano dane")
            return
        } 
        
        toast.error(`Błąd podczas dodawania firmy - ${res.status}`)
    }
</script>

<Dialog.Root open={true} onOpenChange={(open) => setDialog({code: open ? 1 : 0})}>
    <Dialog.Content class="backdrop-blur-lg">
        <CompanyForm 
            name={companyData[1]}
            email={companyData[2]}
            owner={companyData[3]}
            phone={companyData[4]}
            website={companyData[5]}
            town={companyData[6]}
            street={companyData[7]}
            building={companyData[8]}
            apartment={companyData[9]}
            onSubmit={edit}
        />
    </Dialog.Content>
</Dialog.Root>