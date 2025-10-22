<script>
    import Star from "@lucide/svelte/icons/star";
    import AvatarFallback from "./ui/avatar/avatar-fallback.svelte";
    import Avatar from "./ui/avatar/avatar.svelte";

    let { comment, rating, created_at, user_name } = $props()
    let grades = [1,2,3,4,5]
</script>

<div class="row gap-4 border-b pb-6" style="align-items: start;">
    <Avatar class="mt-2">
        <AvatarFallback class="bg-primary">{user_name[0]}</AvatarFallback>
    </Avatar>
    <div class="column w-full max-w-full" style="align-items: start;">
        <div class="w-full row justify-between">
            <p>{user_name}</p>
            <p class="text-gray-300 text-sm md:text-base">{created_at.toLocaleDateString()}</p>
        </div>
        <div class="row gap-1">
            {#each grades as g}
                <Star class="w-4 {g <= rating ? "text-yellow-300 fill-yellow-300" : "fill-gray-300 text-gray-300"}" />
            {/each}
        </div>
        <p class="w-full flex break-all mt-2 text-wrap">{comment}</p>
    </div>
</div>
