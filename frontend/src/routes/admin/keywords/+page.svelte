<script lang="ts">
    import StringListEditor from '$lib/components/StringListEditor.svelte';
    import { fetcher } from '$lib/fetcher';
    import { toast } from 'svelte-sonner';

    let { data } = $props()
    // @ts-ignore
    let categories = data.categories
    
    async function saveKeyWords(cattegoryId: string, keywords: string[]) {
        const res = await fetcher(`/api/admin/keywords/${cattegoryId}`, {
            method: "PATCH",
            body: JSON.stringify({
                keywords: keywords
            })
        })

        if (res.ok) {
            toast.success("Zapisano zmiany")
        }

        if (!res.ok) {
            toast.error("Nie udało się zapisać zmian")
        }
    }

</script>

<div style="height: calc(100vh - 120px);" class="w-[80%] scroll-none overscroll-none mx-auto overflow-y-auto row flex-wrap gap-6">
    {#each categories as c}
        <StringListEditor onChange={(keywords) => saveKeyWords(c.id, keywords)} title={c.name} items={c.keywords} />
    {/each}
</div>
