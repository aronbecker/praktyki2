<script>
    import Star from "@lucide/svelte/icons/star";

    let { stars = $bindable()} = $props()
    let arr = [1,2,3,4,5]
</script>

<div class="row gap-1">
    {#each arr as g}
        <button onclick={() => stars = g}>
            <Star class="w-6 ml-auto hover:text-yellow-300 {g <= stars ? "fill-yellow-300 text-yellow-300" : ""} "/>
        </button>
    {/each}
    <p class="ml-2">{stars}</p>
</div>
