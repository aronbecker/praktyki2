<script>
    let { text, onclick, children } = $props()
</script>

<button onclick={onclick} class="w-full h-18 bg-input/30 cursor-pointer text-xl border text-gray-300 row gap-4 pl-8 hover:bg-input/15">
    {@render children()}
    {text}
</button>
