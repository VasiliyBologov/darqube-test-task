import { loginUrl } from '../components/constants';


export default async function login (name) {
    console.log('bleatttt')
    const url = loginUrl + name;
    const settings = {
        method: 'POST',
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
        }
    };
    try {
        const response = await fetch(url, settings);
        if (response.ok) {
            return await response;
          }
          if (response.status === 401) {
            return {ok: false}
          }
          return Promise.reject(response);
    } catch (e) {
        return e;
    }    
}



