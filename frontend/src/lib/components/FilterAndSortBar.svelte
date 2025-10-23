<script lang="ts">
    import Button from "./ui/button/button.svelte";
    import * as Select from "$lib/components/ui/select/index.js";
    import { getCategories } from "$lib/getCategories";

    let { onChange } = $props();
    
    let categories = $state(["Wszystkie kategorie"]);
    const grades = ["Wszystkie oceny", "5", "4", "3", "2", "1"];

    let category = $derived(categories[0]);
    let rating = $state(grades[0]);
    let categoriesLoaded = $state(false)

    function change() {
        onChange(category, rating);
    }

    function resetFilters() {
        category = categories[0];
        rating = "Wszystkie oceny";
        change();
    }

    async function loadCategories() {
        if (categoriesLoaded) return
        const loadedCategories = await getCategories()
        categories = [...categories, loadedCategories.categories]
        categoriesLoaded = true
    }

</script>

<div class="w-full min-h-18 bg-input/30 p-4 gap-6 border flex-wrap rounded-lg row mx-2 md:mx-7">
    <p class="mr-auto md:mr-0">Kategoria</p>
    <Select.Root type="single" bind:value={category} onValueChange={change}>
        <Select.Trigger onclick={loadCategories} class="w-[180px]">{category}</Select.Trigger>
        <Select.Content>
            {#each categories as cat}
                <Select.Item value={cat}>{cat}</Select.Item>
            {/each}
        </Select.Content>
    </Select.Root>
    <p class="mr-auto md:mr-0">Minimalna Ocena</p>
    <Select.Root type="single" bind:value={rating} onValueChange={change}>
        <Select.Trigger class="w-[180px]">{rating}</Select.Trigger>
        <Select.Content>
            {#each grades as grade}
                <Select.Item value={grade}>{grade}</Select.Item>
            {/each}
        </Select.Content>
    </Select.Root>
    <Button variant="outline" class="ml-auto" onclick={resetFilters}>Resetuj filtry</Button>
</div>
