import api from "./axios";

export const getClusters = async () => {
    const response = await api.get("/clusters");
    return response.data.clusters;
};

export const getClusterById = async (id) => {
    const response = await api.get(`/clusters/${id}`);
    return response.data;
};