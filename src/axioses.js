import axios from "axios";

async function getData() {
  try {
    const response = await axios.get(
      "http://127.0.0.1:8000/gongmo/acontest-list/"
    );
    return response.data;
  } catch (error) {
    throw new Error("Error fetching data:", error);
  }
}
export default getData;
