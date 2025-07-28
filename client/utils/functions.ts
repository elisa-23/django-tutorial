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

export function shuffle<T>(array: T[]): T[] {
    for (let i = array.length - 1; i >= 1; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j]!, array[i]!];
    }
    return array;
}

/** Makes a request to an endpoint.\
 * @param endpoint - The endpoint to request, relative to the API base URL.
 * @param method - The HTTP method to use (GET, POST, etc.). Defaults to GET.
 * @param body - The body of the request, if applicable. Defaults to undefined.
 */
export async function requestEndpoint(endpoint: string, method?: string, body?: object): Promise<void>;
/** Makes a request to an endpoint.\
 * @template T - The expected response type.
 * @param endpoint - The endpoint to request, relative to the API base URL.
 * @param method - The HTTP method to use (GET, POST, etc.). Defaults to GET.
 * @param body - The body of the request, if applicable. Defaults to undefined.
 */
export async function requestEndpoint<T>(endpoint: string, method?: string, body?: object): Promise<T>;
export async function requestEndpoint<T>(endpoint: string, method?: string, body?: object): Promise<T | void> {
  const config = useRuntimeConfig();

  const options: RequestInit = method ? {
    method: method,
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(body),
  } : {};

  const res = await fetch(`${config.public.apiBase}${endpoint}`, options);
  if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);

  return res.json() as T;
}