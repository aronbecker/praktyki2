export async function fetcher(url: string, opts: FetcherOptions) {
    let headers = new Headers()

    if (opts.headers !== undefined) {
        headers = opts.headers
    }

    setIfAbsent(headers, "Content-type", "application/json;charset=UTF-8")

    return await fetch(url, {
        body: opts.method === "GET" ? null : opts.body,
        method: opts.method,
        credentials: opts.credentials ? "include" : "same-origin",
        mode: "cors",
        headers: headers
    })
} 

function setIfAbsent(headers: Headers, header: string, value: string) {
    if (headers.has(header)) return
    headers.set(header, value)
}

export type FetcherOptions = {
    method: "GET" | "POST" | "PATCH" | "PUT" | "DELETE",
    body?: any,
    credentials?: boolean,
    headers?: Headers
}