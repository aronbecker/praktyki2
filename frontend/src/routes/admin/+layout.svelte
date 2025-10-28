<script>
    import { goto } from "$app/navigation";
    import Button from "$lib/components/AdminPanelButton.svelte"
    import Building2 from '@lucide/svelte/icons/building-2'
    import Plus from '@lucide/svelte/icons/plus'
    import ALargeSmall from '@lucide/svelte/icons/a-large-small'

    let { children } = $props()
</script>

<div class="row flex-wrap">
    <div class="md:w-[300px] h-max md:h-[calc(100vh-6rem)] w-full flex-box bg-background/40 column border-r">
        <Button text="Dodaj firmę" onclick={async () => await goto("/admin/addCompany")}>
            <Plus class="text-gray-300"/>
        </Button>
        <Button text="Lista firm" onclick={async () => await goto("/admin/companies")}>
            <Building2 class="text-gray-300"/>
        </Button>
        <Button text="Słowa kluczowe" onclick={async () => await goto("/admin/keywords")}>
            <ALargeSmall class="text-gray-300"/>
        </Button>
    </div>
    {@render children()}
</div>
