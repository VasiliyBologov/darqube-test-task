
import { fetchData } from "./fetchData";

// Get My Subscriptions
export async function get_my_subscriptions() {
  return await new FetchData(`/my`).GET();
}

// Update My Subscriptions
export async function update_my_subscriptions(subscriptions) {
  return await new FetchData(`/my?subscriptions=${subscriptions}`).POST({ subscriptions });
}