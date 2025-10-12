<script>
    import Input from "$lib/components/ui/input/input.svelte";
    import Button from "$lib/components/ui/button/button.svelte";
    import Search from "@lucide/svelte/icons/search";
    
    let text = $state("");
    let { onSearch } = $props();
</script>

<div class="searchBar w-[90%] max-w-[900px] py-[1rem] row h-21">
    <div
        class="row flex bg-input/30 w-full h-full rounded-4xl rounded-r-none border pl-3 ring-offset-background focus-within:ring-1 focus-within:ring-ring focus-within:ring-offset-2"
    >
        <Search class="h-[1.4rem] w-[1.4rem] mx-2 text-muted-foreground" />
        <Input
            class="focus-visible:ring-0 border-none"
            bind:value="{text}"
            placeholder="Wyszukaj specializacjie lub słowo kluczowe"
            style="background: transparent"
        />
    </div>
    <Button class="w-24 h-full text-bold text-white rounded-4xl rounded-l-none" onclick={() => onSearch(text)}>
        Szukaj
    </Button>
</div>

