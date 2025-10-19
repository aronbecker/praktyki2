<script lang="ts" generics="TData, TValue">
 import { getCoreRowModel } from "@tanstack/table-core";
 import {
  createSvelteTable,
  FlexRender,
 } from "$lib/components/ui/data-table/index.js";
 import * as Table from "$lib/components/ui/table/index.js";
    import { columns } from "./columns";
 
 let { companies } = $props()

 const table = createSvelteTable({
  get data() {
   return companies
  },
  columns,
  getCoreRowModel: getCoreRowModel(),
 });
</script>
 
<div class="rounded-md border">
 <Table.Root class="bg-black/30">
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
     <Table.Cell class="text-blue-400 cursor-pointer" onclick={() => alert("Edytuj")}>
        Edytuj
     </Table.Cell>
     <Table.Cell class="text-red-400 cursor-pointer" onclick={() => alert("Usuń")}>
        Usuń
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