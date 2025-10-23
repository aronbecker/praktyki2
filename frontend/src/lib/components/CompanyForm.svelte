<script lang="ts">
    import { Button } from "$lib/components/ui/button";
    import Input from "$lib/components/ui/input/input.svelte";
    import { Validator } from "$lib/validator";

    const inputStyles = "h-12"
    const doubleInputWrapper = "row gap-2"
    const descriptinonStyles = "mr-auto ml-2"
    
    const validator = new Validator()
    let isFormValid = $state(false)

    let {
        name = "",
        owner = "",
        phone = "",
        email = "",
        website = "",
        town = "",
        street = "",
        building = "",
        apartment = "",
        categories = [],
        nip = "",
        regon = "",
        onSubmit
    } = $props()

    let newCategory = $state("")

    validator.addField("name", () => name, (str) => str.length > 2)
    validator.addField("owner", () => owner, (str) => str.length > 1)
    validator.addField("phone", () => phone, 
        (str) => str.replaceAll(" ", "").length == 9 || str.length == 0)
    validator.addField("town", () => town, (str) => str.length > 3)
    validator.addField("street", () => street, (str) => str.length > 2)
    validator.addField("building", () => building, (str) => str.length > 0)
    validator.addField("nip", () => nip, (str) => str.length == 10)
    validator.addField("regon", () => regon, (str) => 7 <= str.length && str.length < 10)

    function validate() {
        isFormValid = validator.isValid()
    }

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

    async function submit() {
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
            categories: categories,
            nip: nip,
            regon: regon
        }
        await onSubmit(payload)
    }
</script>

<form oninput={validate} class="column m-auto gap-4 p-4 overflow-auto">
    <h2 class="text-center font-bold text-3xl text-gray-300 mb-6">Dodawania/Edycja firmy</h2>
    <p class={descriptinonStyles}>Informacje podstawowe</p>
    <Input bind:value={name} class={inputStyles} placeholder="Nazwa" type="text" />
    <div class={doubleInputWrapper}>
        <Input bind:value={nip} class={inputStyles} placeholder="Nip" type="text" maxlength={10}/>
        <Input bind:value={regon} class={inputStyles} placeholder="Regon" type="text" maxlength={9} />
    </div>
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
                <button class="ml-2 text-sm text-red-300" aria-label="Usuń kategorię" onclick={() => removeCategory(i)}>✕</button>
            </div>
        {/each}
        {#if categories.length === 0}
            <p class="text-muted-foreground">Brak kategorii — dodaj pierwszą</p>
        {/if}
    </div>

    <Button onclick={submit} disabled={!isFormValid} class="w-full h-12">Zatwierdź</Button>
</form>