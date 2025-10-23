<script lang="ts">
    import Button from "$lib/components/ui/button/button.svelte";
    import Card from "$lib/components/ui/card/card.svelte";
    import Phone from "@lucide/svelte/icons/phone";
    import Star from "@lucide/svelte/icons/star";
    import Email from "@lucide/svelte/icons/mail";
    import Globe from "@lucide/svelte/icons/globe";
    import User from "@lucide/svelte/icons/user";
    import MapPin from "@lucide/svelte/icons/map-pin";
    import MessageCircle from "@lucide/svelte/icons/message-circle"
    import Textarea from "$lib/components/ui/textarea/textarea.svelte";
    import StarRating from "$lib/components/StarRating.svelte";
    import Comment from "$lib/components/Comment.svelte";
    import { fetcher } from "$lib/fetcher.js";
    import { toast } from "svelte-sonner";
    import { userStore } from "$lib/stores/userStore.js";
    import { get } from "svelte/store";
    import type { OpinionDto } from "$lib/dtos/opinionDto.js";

    let { data } = $props()
    const company = (data.company)
    const address = company.address
    const bgColor = "bg-input/30"
    const me = get(userStore)

    let starsInput = $state(0)
    let comment = $state("")
    let comments: OpinionDto[] = $state(data.comments.comments)
    
    const hasWebsite = company.website_url && company.website_url != ""
    const hasEmail = company.email && company.email != ""
    const hasPhone = company.phone_number && company.phone_number != ""

    const stars: Number[] = []
    for (let i = 0; i < Math.floor(company.rating); i++) {
        stars.push(0)
    }

    async function publishComment() {
        const json = JSON.stringify({
            rating: starsInput,
            comment: comment
        })
        
        const response = await fetcher(`/api/comments?companyId=${company.id}`, {
            method: "POST",
            body: json,
        })

        if (response.ok) {
            toast.success("Dodano opinie")
            const newComment: OpinionDto = {
                id: -1,
                comment: comment,
                rating: starsInput,
                creation_date: String(Date.now()),
                user_name: me?.firstname + " " + me?.lastname
            }
            comments = [newComment, ...comments]
            starsInput = 0
            comment = ""
            return
        } else if (response.status === 409) {
            toast.error("Wystawiłeś już opinie tej firmie")
            return
        } else {
            toast.error("Wystąpił bład podczas publikowania komentarza, spróbuj później")
            return
        }
    }
</script>

<div class="column max-w-[1200px] w-full p-[30px] gap-4 mx-auto">
    <Card class="w-full column {bgColor} px-6">
        <div class="flex flex-wrap gap-6 mr-auto w-full">
            <h1 class="font-bold text-4xl mr-auto">{company.name}</h1>
            {#if company.rating > 0}
                <div class="row w-max gap-2">
                    {#each stars as s}
                        <Star class="w-4 ml-auto" color="gold" fill="gold"/>
                    {/each}
                    {company.rating}.0 <span class="text-gray-400 text-sm">({company.ratingCount})</span>
                </div>    
            {/if}
        </div>
        <div class="row flex-wrap gap-4">
            <Button class="w-[300px] h-12 justify-start" variant="outline">
                <Phone class="text-primary" />
                {hasPhone ? company.phone_number : "Brak numeru telefonu"}
            </Button>
            <Button class="w-[300px] h-12 justify-start" variant="outline">
                <Email class="text-primary"/>
                {hasEmail ? company.email : "Brak email"}
            </Button>
            <Button class="w-[300px] h-12 justify-start" href={hasWebsite ? `https://${company.website_url}` : ""} variant="outline">
                <Globe class="text-primary"/>
                <p class="overflow-hidden">{hasWebsite ? company.website_url : "Brak strony www"}</p>
            </Button>
        </div>
    </Card>
    <div class="row w-full flex-wrap md:flex-nowrap gap-4">
        <Card class="w-full h-32 {bgColor} p-6">
            <div class="row gap-4">
                <User class="text-primary" />
                <p class="text-xl font-bold">Właściciel</p>
            </div>
            <p class="ml-2 text-gray-300">{company.owner_name}</p>
        </Card>
        <Card class="w-full h-32 {bgColor} p-6">
            <div class="row gap-4">
                <MapPin class="text-primary" />
                <p class="text-xl font-bold">Lokalizacja</p>
            </div>
            <p class="ml-2 text-gray-300">{address.town}, {address.street} {address.buildingNumber}/{address.apartmentNumber}</p>
        </Card>
    </div>
    <Card class="w-full {bgColor} p-6">
        <div class="row gap-4 mb-6">
            <MessageCircle class="text-primary" />
            <p class="text-xl font-bold">Opinie</p>
        </div>

        {#if data.isAuth}
            <StarRating bind:stars={starsInput} />
            <Textarea bind:value={comment} class="max-w-[400px] resize-none" placeholder="Tutaj wpisz komentarz" />
            <Button disabled={starsInput==0} onclick={publishComment} class="w-28 h-10 mb-6">Opublikuj</Button>
        {/if}

        {#each comments as c}
            <Comment comment={c.comment} rating={c.rating} created_at={new Date(c.creation_date)} user_name={c.user_name} />
        {/each}
    </Card>
</div>