import baseUrl from '../components/constants';


export class fetchData {
  constructor(path) {
    this._url = baseUrl + path;
  }
  GET = async (
    request = {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
      credentials: "include",
    }
  ) => {
    const response = await fetch(this._url, request);
    if (response.ok) {
      return await response.json();
    }
    if (response.status === 401) {
      auth.forceLogout();
    }
    return Promise.reject(response);
  }
  POST = async(
    data,
    request = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data ?? ""),
      credentials: "include",
    }
  ) => {
    const response = await fetch(this._url, request);
    if (response.ok) {
      return await response.json();
    }
    if (response.status === 401) {
      auth.forceLogout();
    }
    return Promise.reject(response);
  }
};
export default fetchData