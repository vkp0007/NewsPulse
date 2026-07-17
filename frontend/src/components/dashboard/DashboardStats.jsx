function DashboardStats({
  articles,
  clusters,
}) {

  const lastUpdated =
    articles.length > 0
      ? new Date(
          Math.max(
            ...articles.map((article) =>
              new Date(article.created_at).getTime()
            )
          )
        ).toLocaleString([], {
          dateStyle: "medium",
          timeStyle: "short",
        })
      : "N/A";

  const stats = [
    {
      label: "Articles",
      value: articles.length,
    },
    {
      label: "Clusters",
      value: clusters.length,
    },
    {
      label: "Today",
      value: articles.filter((article) => {
        const today = new Date().toDateString();

        return (
          new Date(article.created_at).toDateString() === today
        );
      }).length,
    },
    {
      label: "Last Updated",
      value: lastUpdated,
    },
  ];

  return (
    <section className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
      {stats.map((stat) => (
        <div
          key={stat.label}
          className="rounded-2xl border border-slate-200 bg-white p-8 transition-all duration-300 hover:-translate-y-1 hover:border-black hover:shadow-sm"
        >
          <p className="text-sm uppercase tracking-wider text-slate-500">
            {stat.label}
          </p>

          <h2
            className={`mt-3 font-bold text-black ${
              stat.label === "Last Updated"
                ? "text-xl leading-8"
                : "text-4xl"
            }`}
          >
            {stat.value}
          </h2>
        </div>
      ))}
    </section>
  );
}

export default DashboardStats;