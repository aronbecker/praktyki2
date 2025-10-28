
<script lang="ts">
  export let title: string
  export let items: string[] = [];
  export let onChange: (items: string[]) => void
  let newItem = '';

  function addItem() {
    const trimmed = newItem.trim();
    if (!trimmed) return;
    if (items.includes(trimmed)) {
      newItem = '';
      return;
    }
    items = [...items, trimmed];
    newItem = '';
    onChange(items)
  }

  function removeItem(index: number) {
    items = items.filter((_, i) => i !== index);
    onChange(items)
  }

  function handleKeyDown(e: KeyboardEvent) {
    if (e.key === 'Enter') {
      e.preventDefault();
      addItem();
    }
  }
</script>

<div class="space-y-3 bg-black/20 rounded-2xl shadow-sm p-4">
  <h3 class="text-lg font-semibold">{title} </h3>

  <div class="flex items-center gap-2">
    <input
      class="flex-1 rounded-md border px-3 py-2 text-sm"
      placeholder="Dodaj słowo kluczowe"
      bind:value={newItem}
      on:keydown={handleKeyDown}
    />
    <button class="rounded-md px-3 py-2 border text-sm" on:click={addItem}>Dodaj</button>
  </div>

  {#if items.length === 0}
    <p class="text-sm text-slate-500">Brak elementów</p>
  {:else}
    <ul class="list-disc ml-5 space-y-1">
      {#each items as item, index}
        <li class="flex items-center justify-between">
          <span>{item}</span>
          <button class="text-xs text-red-600 hover:underline" on:click={() => removeItem(index)}>Usuń</button>
        </li>
      {/each}
    </ul>
  {/if}
</div>
