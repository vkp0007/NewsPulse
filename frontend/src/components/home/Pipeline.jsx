function Pipeline() {
  const steps = [
    {
      number: "01",
      title: "Collect",
      description:
        "Continuously ingests articles from trusted publishers.",
    },
    {
      number: "02",
      title: "Embed",
      description:
        "Generates semantic embeddings using Sentence Transformers.",
    },
    {
      number: "03",
      title: "Compare",
      description:
        "Computes similarity using embeddings, keywords and entities.",
    },
    {
      number: "04",
      title: "Cluster",
      description:
        "Groups related articles into evolving news events.",
    },
    {
      number: "05",
      title: "Update",
      description:
        "Keeps clusters updated as new articles arrive.",
    },
  ];

  return (
    <section id="pipeline" className="space-y-12">
      <div className="mx-auto max-w-3xl text-center">
        <p className="text-sm font-medium uppercase tracking-[0.2em] text-slate-500">
          How It Works
        </p>

        <h2 className="mt-4 text-4xl font-bold tracking-tight text-black lg:text-5xl">
          From Articles to Stories
        </h2>

        <p className="mx-auto mt-5 max-w-2xl text-lg leading-8 text-slate-600">
          Every incoming article passes through an intelligent pipeline before
          becoming part of an evolving news story.
        </p>
      </div>

      <div className="grid gap-5 md:grid-cols-2 xl:grid-cols-5">
        {steps.map((step) => (
          <div
            key={step.number}
            className="group rounded-2xl border border-slate-200 bg-white p-6 transition-all duration-300 hover:-translate-y-1 hover:border-black"
          >
            <span className="text-xs font-semibold tracking-[0.2em] text-slate-400 transition group-hover:text-black">
              {step.number}
            </span>

            <h3 className="mt-4 text-xl font-semibold text-black">
              {step.title}
            </h3>

            <p className="mt-4 text-sm leading-7 text-slate-600">
              {step.description}
            </p>
          </div>
        ))}
      </div>
    </section>
  );
}

export default Pipeline;