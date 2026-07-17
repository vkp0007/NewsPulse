import ClusterCard from "./ClusterCard";
import ArticleCard from "../cluster/ArticleCard";

function ClusterGrid({
  clusters,
  searchQuery,
  setSearchQuery,
  searchResults,
}) {
  return (
    <section>

      <div className="mb-6 flex flex-col gap-6 lg:flex-row lg:items-end lg:justify-between">

        <div>

          <h2 className="text-3xl font-bold tracking-tight text-black">
            News Clusters
          </h2>

          <p className="mt-2 text-slate-600">
            Browse AI-organized stories aggregated from trusted news publishers.
          </p>

        </div>

        <div className="flex w-full max-w-md gap-3">

          <input
            type="text"
            placeholder="Search articles..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="flex-1 rounded-xl border border-slate-300 px-4 py-2.5 outline-none transition focus:border-black"
          />

        </div>

      </div>

      {searchQuery.trim() && (
        <section className="mb-10">

          <div className="mb-6 flex items-center justify-between">

            <h3 className="text-2xl font-bold tracking-tight text-black">
              Search Results
            </h3>

            <span className="rounded-full bg-black px-4 py-2 text-sm font-medium text-white">
              {searchResults.length} Results
            </span>

          </div>

          {searchResults.length === 0 ? (
            <div className="rounded-2xl border border-dashed border-slate-300 py-16 text-center">
              <p className="text-slate-500">
                No matching articles found.
              </p>
            </div>
          ) : (
            <div className="mb-10 grid gap-6 lg:grid-cols-2">
              {searchResults.map((article) => (
                <ArticleCard
                  key={article._id}
                  article={article}
                />
              ))}
            </div>
          )}

        </section>
      )}

      <div className="mb-6 flex items-end justify-between">

        <h3 className="text-2xl font-bold tracking-tight text-black">
          Trending Clusters
        </h3>

        <span className="rounded-full bg-black px-4 py-2 text-sm font-medium text-white">
          {clusters.length} Clusters
        </span>

      </div>

      {clusters.length === 0 ? (
        <div className="rounded-2xl border border-dashed border-slate-300 py-20 text-center">
          <p className="text-slate-500">
            No clusters available.
          </p>
        </div>
      ) : (
        <div className="grid gap-6 lg:grid-cols-2 2xl:grid-cols-3">
          {clusters.map((cluster) => (
            <ClusterCard
              key={cluster._id}
              cluster={cluster}
            />
          ))}
        </div>
      )}

    </section>
  );
}

export default ClusterGrid;