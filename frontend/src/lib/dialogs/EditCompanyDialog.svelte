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
            nip={companyData[1]}
            regon={companyData[2]}
            name={companyData[3]}
            email={companyData[4]}
            owner={companyData[5]}
            phone={companyData[6]}
            website={companyData[7]}
            town={companyData[8]}
            street={companyData[9]}
            building={companyData[10]}
            apartment={companyData[11]}
            onSubmit={edit}
        />
    </Dialog.Content>
</Dialog.Root>