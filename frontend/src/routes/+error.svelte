<script>
	import { page } from '$app/state';
    import Button from '$lib/components/ui/button/button.svelte';

    let message = "Nastąpił nieznany błąd"

    if (page.status == 404) {
        message = "Nie znaleziono tej strony"
    }
</script>

<div class="column inset-0 absolute m-auto h-max">
    <h1 class="mb-6 text-4xl px-4 text-center">
        {message}
    </h1>
    <Button variant="link" href="/">Powrót na stronę główną</Button>
</div>
