import { useEffect, useState } from "react";
import { useParams } from "react-router";

import { getClusterById } from "../services/clusterApi";

import ClusterHeader from "../components/cluster/ClusterHeader";



import ArticleList from "../components/cluster/ArticleList";

function ClusterDetails() {

    const { id } = useParams();

    const [cluster, setCluster] = useState(null);
    const [articles, setArticles] = useState([]);

    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    useEffect(() => {

        const fetchCluster = async () => {

            try {

                const data = await getClusterById(id);

                console.log(data);

                setCluster(data.cluster);
                setArticles(data.articles);

            } catch (err) {

                console.error(err);
                setError("Failed to load cluster.");

            } finally {

                setLoading(false);

            }

        };

        fetchCluster();

    }, [id]);

    if (loading) {
        return (
            <div className="py-20 text-center">
                Loading cluster...
            </div>
        );
    }

    if (error) {
        return (
            <div className="py-20 text-center text-red-500">
                {error}
            </div>
        );
    }

    if (!cluster) {
        return (
            <div className="py-20 text-center">
                Cluster not found.
            </div>
        );
    }

    return (

        <div className="space-y-10">

            <ClusterHeader
                cluster={cluster}
            />

       
            <ArticleList
                articles={articles || []}
            />

        </div>

    );

}

export default ClusterDetails;