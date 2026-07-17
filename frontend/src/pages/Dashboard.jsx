import { useEffect, useState } from "react";

import DashboardStats from "../components/dashboard/DashboardStats";
import DashboardSkeleton from "../components/dashboard/DashboardSkeleton";
import ClusterGrid from "../components/cluster/ClusterGrid";

import { getClusters } from "../services/clusterApi";
import { getArticles } from "../services/articleApi";

function Dashboard() {
  const [clusters, setClusters] = useState([]);
  const [articles, setArticles] = useState([]);

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  // Search state
  const [searchQuery, setSearchQuery] = useState("");

  useEffect(() => {
    const fetchDashboardData = async () => {
      try {
        const [clusterData, articleData] = await Promise.all([
          getClusters(),
          getArticles(),
        ]);

        setClusters(clusterData);
        setArticles(articleData);
      } catch (err) {
        console.error(err);
        setError("Failed to load dashboard.");
      } finally {
        setLoading(false);
      }
    };

    fetchDashboardData();
  }, []);

  // Filter articles locally
  const searchResults = searchQuery.trim()
    ? articles.filter((article) => {
        const query = searchQuery.toLowerCase();

        return (
          article.title?.toLowerCase().includes(query) ||
          article.summary?.toLowerCase().includes(query) ||
          article.source?.toLowerCase().includes(query)
        );
      })
    : [];

  if (loading) return <DashboardSkeleton />;

  if (error) {
    return (
      <div className="py-20 text-center text-red-500">
        {error}
      </div>
    );
  }

  return (
    <div className="space-y-10">

      <div className="py-5">
        <h1 className="text-4xl font-bold tracking-tight text-black">
          Dashboard
        </h1>

        <p className="mt-2 text-lg text-slate-600">
          Monitor AI-clustered global news events in real time.
        </p>
      </div>

      <DashboardStats
        articles={articles}
        clusters={clusters}
      />

      <ClusterGrid
        clusters={clusters}
        searchQuery={searchQuery}
        setSearchQuery={setSearchQuery}
        searchResults={searchResults}
      />

    </div>
  );
}

export default Dashboard;