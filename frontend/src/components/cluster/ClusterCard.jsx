import { Link } from "react-router";

function ClusterCard({ cluster }) {
  const sources = cluster.sources || [];

  return (
    <Link
      to={`/clusters/${cluster._id}`}
      className="group block h-full rounded-3xl border border-slate-200 bg-white p-7 transition-all duration-300 hover:-translate-y-1 hover:border-black hover:shadow-md"
    >
      <div className="flex items-start justify-between gap-4">
        <h2 className="flex-1 text-2xl font-semibold leading-8 tracking-tight text-black">
          {cluster.title}
        </h2>

        <div className="flex shrink-0 flex-wrap justify-end gap-2">
          {sources.slice(0, 2).map((source) => (
            <span
              key={source}
              className="rounded-full border border-red-200 bg-red-50 px-3 py-1 text-xs font-semibold text-red-700"
            >
              {source}
            </span>
          ))}

          {sources.length > 2 && (
            <span className="rounded-full border border-slate-200 bg-slate-100 px-3 py-1 text-xs font-semibold text-slate-600">
              +{sources.length - 2}
            </span>
          )}
        </div>
      </div>

      <p className="mt-5 line-clamp-3 text-[15px] leading-7 text-slate-600">
        {cluster.summary}
      </p>
    </Link>
  );
}

export default ClusterCard;