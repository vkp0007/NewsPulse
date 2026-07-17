import { Link } from "react-router";

function Footer() {
  return (
    <footer className="border-t border-slate-200 py-6">
      <div className="flex flex-col items-center justify-between gap-4 lg:flex-row">
        <div>
          <h3 className="font-semibold text-black">
            NewsPulse AI
          </h3>

          <p className="mt-1 text-sm text-slate-500">
            AI-powered news intelligence platform
          </p>
        </div>

        <div className="flex gap-8 text-sm text-slate-600">
          <Link
            to="/"
            className="transition hover:text-black"
          >
            Home
          </Link>

          <Link
            to="/dashboard"
            className="transition hover:text-black"
          >
            Dashboard
          </Link>
        </div>

        <p className="text-sm text-slate-500">
          © 2026 Vinay Patel
        </p>
      </div>
    </footer>
  );
}

export default Footer;