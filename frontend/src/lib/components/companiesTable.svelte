<script lang="ts" generics="TData, TValue">
 import { getCoreRowModel } from "@tanstack/table-core";
 import {
  createSvelteTable,
  FlexRender,
 } from "$lib/components/ui/data-table/index.js";
 import * as Table from "$lib/components/ui/table/index.js";
 import { columns } from "./columns";
 import Trash from "@lucide/svelte/icons/trash"
 import Pencil from "@lucide/svelte/icons/pencil"
    import { fetcher } from "$lib/fetcher";
    import { toast } from "svelte-sonner";
    import { setDialog } from "$lib/stores/dialogStore";

 let { companies } = $props()

 const table = createSvelteTable({
  get data() {
   return companies
  },
  columns,
  getCoreRowModel: getCoreRowModel(),
 });

 function openEditCompanyDialog(data: any) {
   const values: any[] = []
   data.forEach((d:any) => {
      values.push(d.getValue())
   })
   setDialog({
      code: 2,
      data: {
         companyData: values
      }
   })
 }

 async function deleteCompany(id: unknown) {
   const res = await fetcher(`/api/admin/company/${id}`, {
      method: "DELETE",
   })

   if (!res.ok) {
      toast.error(`Błąd podczas usuwania firmy - ${res.status}`)
      return
   }

   toast.success("Usunięto firmę")
   companies = companies.filter((c: any) => c.id !== id)
 }
</script>
 
<div class="rounded-xl border">
 <Table.Root class="bg-black/10 rounded-xl">
  <Table.Header class="w-full">
   {#each table.getHeaderGroups() as headerGroup (headerGroup.id)}
    <Table.Row>
     {#each headerGroup.headers as header (header.id)}
      <Table.Head class="px-6"  colspan={header.colSpan}>
       {#if !header.isPlaceholder}
        <FlexRender
         content={header.column.columnDef.header}
         context={header.getContext()}
        />
       {/if}
      </Table.Head>
     {/each}
    </Table.Row>
   {/each}
  </Table.Header>
  <Table.Body>
   {#each table.getRowModel().rows as row (row.id)}
    <Table.Row data-state={row.getIsSelected() && "selected"}>
     {#each row.getVisibleCells() as cell (cell.id)}
      <Table.Cell class="px-6 max-w-[200px] overflow-auto">
       <FlexRender
        content={cell.column.columnDef.cell}
        context={cell.getContext()}
       />
      </Table.Cell>
     {/each}
     <Table.Cell onclick={() => openEditCompanyDialog(row.getVisibleCells())} class="text-blue-400 w-12 cursor-pointer">
        <Pencil class="w-4 mx-auto" />
     </Table.Cell>
     <Table.Cell class="text-red-500 w-12 cursor-pointer" onclick={() => deleteCompany(row.getVisibleCells().at(0)?.getValue())}>
        <Trash class="w-4 mx-auto" />
     </Table.Cell>
    </Table.Row>
   {:else}
    <Table.Row>
     <Table.Cell colspan={columns.length} class="h-24 text-center">
      Brak wyników
     </Table.Cell>
    </Table.Row>
   {/each}
  </Table.Body>
 </Table.Root>
</div>