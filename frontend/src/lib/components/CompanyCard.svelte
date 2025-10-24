<script lang="ts">
    import type { CompanyDto } from "$lib/dtos/companyDto";
    import * as Card from "$lib/components/ui/card/index.js";
    import Star from "@lucide/svelte/icons/star";
    import Location from "@lucide/svelte/icons/map-pin";
    import Letter from "@lucide/svelte/icons/mail";
    import Globe from "@lucide/svelte/icons/globe";
    import Phone from "@lucide/svelte/icons/phone";
    import { goto } from "$app/navigation";
    import Badge from "./ui/badge/badge.svelte";

    let company: CompanyDto = $$props.company;

    const address = company.address;

    const color = "text-gray-300";
    const iconsStyles = "w-4 " + color;
    const rowStyle = "row gap-2 max-w-full overflow-hidden";

    async function redirect() {
        await goto(`/firma/${company.id}`)
    }

</script>

<Card.Root onclick={redirect} class="bg-input/30 max-w-[360px] min-h-[230px] rounded-xl w-full hover:scale-[1.02] transition-transform">
    <Card.Header>
        <div class="{rowStyle} mb-2">
            <Card.Title class="text-lg">{company.name}</Card.Title>
            {#if company.rating}
                <Star class="w-4 ml-auto" color="gold" fill="gold"/>
                <p class={color}>{company.rating}.0 <span class="text-gray-400 text-sm">({company.ratingCount})</span></p>
            {/if}
        </div>
        <div class="row flex-wrap gap-2 gap-y-4">
            {#each company.categories as c}
                <Badge class="text-white bg-blue-500">
                    {c}
                </Badge>
            {/each}
        </div>
    </Card.Header>
    <Card.Content class="space-y-2">
        <div class={rowStyle}>
            <Location class={iconsStyles} />
            <p class={color}>{address.town}, {address.street} {address.buildingNumber}{address.apartmentNumber ? "/" + address.apartmentNumber : ""}</p>
        </div>
        {#if company.phone_number}
            <div class={rowStyle}>
                <Phone class={iconsStyles} />
                <p class="{color} text-white">{company.phone_number}</p>
            </div>
        {/if}
        {#if company.email}
            <div class={rowStyle}>
                <Letter class={iconsStyles} />
                <p class={color}>{company.email}</p>
            </div>
        {/if}
        {#if company.website_url}
            <div class={rowStyle}>
                <Globe class={iconsStyles} />
                <a target="_blank" href="https://{company.website_url}" class="{color} text-primary max-w-[130px]">{company.website_url}</a>
            </div>
        {/if}
    </Card.Content> 
</Card.Root>