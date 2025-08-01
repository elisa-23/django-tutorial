/**
 * Fetches JSON data from a given endpoint.
 *
 * @remarks
 * This function is a wrapper around the Fetch API that adds the base URL
 * from the Nuxt configuration and handles errors.
 *
 * @param endpoint - The relative URL of the endpoint to fetch.
 * @returns The JSON data from the endpoint as a Promise of type T.
 * @throws {Error} If the response was not OK.
 */
/* export async function fetchEndpoint(url: string, method?: string, body?: object) {
    const config = useRuntimeConfig();
    const response = await $fetch(`${config.public.apiBaseUrl}${url}`, {
        method: method,
        body: body,
    });

    return response;
} */

/**
* Fetches JSON data from a given endpoint.
*
* @remarks
* This function is a wrapper around the Fetch API that adds the base URL
* from the Nuxt configuration and handles errors.
*
* @param url - The relative URL of the endpoint to fetch.
* @param method - The request method to use. Defaults to 'GET'.
* @param body - The request body to send with the request. Only applicable
* for non-GET requests.
* @param params - The request parameters to send with the request. Only applicable
* for GET requests.
* @returns The JSON data from the endpoint as a Promise of type T.
* @throws {Error} If the response was not OK.
*/
export async function fetchEndpoint(     //<T> a parameter
    url: string,
    method?: string,
    body?: object,
    params?: Record<string, any>
): Promise<void>;
/**
 * Fetches JSON data from a given endpoint.
 *
 * @remarks
 * This function is a wrapper around the Fetch API that adds the base URL
 * from the Nuxt configuration and handles errors.
 * @template T - The type of the data to be returned from the endpoint.
 * @param url - The relative URL of the endpoint to fetch.
 * @param method - The request method to use. Defaults to 'GET'.
 * @param body - The request body to send with the request. Only applicable
 * for non-GET requests.
 * @param params - The request parameters to send with the request. Only applicable
 * for GET requests.
 * @returns The JSON data from the endpoint as a Promise of type T.
 * @throws {Error} If the response was not OK.
 */
export async function fetchEndpoint<T>(     //<T> a parameter
    url: string,
    method?: string,
    body?: object,
    params?: Record<string, any>
): Promise<T>;
export async function fetchEndpoint<T>(     //<T> a parameter
    url: string,
    method = 'GET',
    body?: object,
    params?: Record<string, any>
): Promise<T | void> {
    const config = useRuntimeConfig();

    const options: any = {
        method,
        params,
    };

    if (body && method !== 'GET') {
        options.body = body;
    }

    try {
        return await $fetch(`${config.public.apiBaseUrl}${url}`, options) as T;
    } catch (error: any) {
        console.error(`Error fetching ${url}:`, error?.data || error?.message || error);
        throw error;
    }
}
