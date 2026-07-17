import { Link } from "react-router";

function Hero() {
  const features = [
    {
      title: "AI Clustering",
      description: "Groups related articles into evolving news stories.",
    },
    {
      title: "Duplicate Detection",
      description: "Removes duplicate content using semantic similarity.",
    },
    {
      title: "Multi-Source",
      description: "Aggregates coverage from trusted publishers.",
    },
    {
      title: "Real-time Updates",
      description: "Continuously refreshes clusters as news develops.",
    },
  ];

  return (
    <section className="grid items-center gap-12 py-2 lg:grid-cols-[1.15fr_0.85fr]">
      {/* Left */}
      <div>
    

        <h1 className="mt-6 text-5xl font-bold leading-tight tracking-tight text-black lg:text-6xl">
          Monitor global news,
          <br />
          <span className="text-slate-400">
            not individual articles.
          </span>
        </h1>

        <p className="mt-6 max-w-2xl text-lg leading-8 text-slate-600">
          NewsPulse AI groups related news from multiple trusted publishers into
          evolving stories using semantic similarity, natural language
          processing and intelligent clustering.
        </p>

        <div className="mt-10 flex flex-wrap gap-4">
          <Link
            to="/dashboard"
            className="rounded-xl bg-black px-6 py-3.5 font-medium text-white transition-all duration-300 hover:-translate-y-0.5 hover:bg-slate-800"
          >
            Explore Dashboard
          </Link>

          <a
            href="#pipeline"
            className="rounded-xl border border-slate-300 px-6 py-3.5 font-medium transition-all duration-300 hover:-translate-y-0.5 hover:bg-slate-100"
          >
            Learn More
          </a>
        </div>
      </div>

      {/* Right */}
      <div className="grid gap-4 sm:grid-cols-2">
        {features.map((feature, index) => (
          <div
            key={feature.title}
            className="group rounded-2xl border border-slate-200 bg-white p-6 transition-all duration-300 hover:-translate-y-1 hover:border-black"
          >
            <span className="text-xs font-semibold tracking-[0.2em] text-slate-400 transition group-hover:text-black">
              0{index + 1}
            </span>

            <h3 className="mt-3 text-lg font-semibold text-black">
              {feature.title}
            </h3>

            <p className="mt-3 text-sm leading-6 text-slate-600">
              {feature.description}
            </p>
          </div>
        ))}
      </div>
    </section>
  );
}

export default Hero;