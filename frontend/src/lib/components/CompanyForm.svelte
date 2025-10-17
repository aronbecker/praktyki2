<script lang="ts">
    import { Button } from "$lib/components/ui/button";
    import Input from "$lib/components/ui/input/input.svelte";
    import { fetcher } from "$lib/fetcher";
    import { toast } from "svelte-sonner";

    const inputStyles = "h-12"
    const doubleInputWrapper = "row gap-2"
    const descriptinonStyles = "mr-auto ml-2"

    let name = ""
    let owner = ""
    let phone = ""
    let email = ""
    let website = ""
    let town = ""
    let street = ""
    let building = ""
    let apartment = ""

    let categories: String[] = []
    let newCategory = ""

    function addCategory() {
        const cat = (newCategory || "").trim()
        if (!cat) return
        if (!categories.includes(cat)) {
            categories = [...categories, cat]
        }
        newCategory = ""
    }

    function removeCategory(index: number) {
        categories = categories.filter((_, i) => i !== index)
    }

    function onCategoryKeydown(e: KeyboardEvent) {
            if (e.key === "Enter") {
                e.preventDefault()
                addCategory()
            }
        }

    async function create() {
        const payload = {
            name: name,
            ownerName: owner,
            phoneNumber: phone,
            email: email,
            website: website,
            town: town,
            street: street,
            building_number: building,
            apartment_number: apartment,
            categories: categories
        }
        
        const res = await fetcher("/api/admin/addCompany", {
            method: "POST",
            body: JSON.stringify(payload)
        })

        if (res.ok) {
            toast.success("Dodano nową firmę")
            return
        } 
        
        toast.error(`Błąd podczas dodawania firmy - ${res.status}`)
    }
</script>

<div class="column m-auto gap-4 p-4 overflow-auto">
    <h2 class="text-center font-bold text-3xl text-gray-300 mb-6">Formularz <br> dodawania nowej firmy</h2>
    <p class={descriptinonStyles}>Informacje podstawowe</p>
    <Input bind:value={name} class={inputStyles} placeholder="Nazwa" type="text" />
    <div class={doubleInputWrapper}>
        <Input bind:value={owner} class={inputStyles} placeholder="Imie i nazwisko właściciela" type="text" />
        <Input bind:value={phone} class={inputStyles} placeholder="Numer telefonu (opcjonalne)" type="tel" />
    </div>
    <div class={doubleInputWrapper}>
        <Input bind:value={email} class={inputStyles} placeholder="Email (opcjonalne)" type="email" />
        <Input bind:value={website} class={inputStyles} placeholder="Strona www (opcjonalne)" type="url" />
    </div>
    <p class={descriptinonStyles}>Adres</p>
    <div class={doubleInputWrapper}>
        <Input bind:value={town} class={inputStyles} placeholder="Miejscowość" type="text" />
        <Input bind:value={street} class={inputStyles} placeholder="Ulica" type="text" />
    </div>
    <div class={doubleInputWrapper}>
        <Input bind:value={building} class={inputStyles} placeholder="Numer budynku" type="text" />
        <Input bind:value={apartment} class={inputStyles} placeholder="Numer lokalu (opcjonalne)" type="number" />
    </div>

    <p class={descriptinonStyles}>Kategorie</p>

    <div class="row gap-2 items-center w-full max-w-[600px]">
        <Input
            class="h-12 flex-1"
            placeholder="Wpisz kategorię i kliknij Dodaj"
            bind:value={newCategory}
            onkeydown={onCategoryKeydown}
        />
        <Button class="h-12" onclick={addCategory}>Dodaj</Button>
    </div>

    <div class="row gap-2 flex-wrap mt-2 max-w-[360px]">
        {#each categories as cat, i}
            <div class="row items-center gap-2 px-3 py-1 rounded-full bg-gray-700 text-white">
                <span>{cat}</span>
                <button class="ml-2 text-sm text-red-300" aria-label="Usuń kategorię" on:click={() => removeCategory(i)}>✕</button>
            </div>
        {/each}
        {#if categories.length === 0}
            <p class="text-muted-foreground">Brak kategorii — dodaj pierwszą</p>
        {/if}
    </div>

    <Button onclick={create} class="w-full h-12">Stwórz</Button>
</div>