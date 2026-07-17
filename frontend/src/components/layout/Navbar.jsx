import { NavLink } from "react-router";

function Navbar() {
  return (
    <header className="sticky top-0 z-50 border-b border-slate-200 bg-white/90 backdrop-blur">
      <div className="mx-auto flex h-14 max-w-7xl items-center justify-between px-8">

        <NavLink
          to="/"
          className="text-xl font-bold tracking-tight text-black"
        >
          NewsPulse AI
        </NavLink>

        <nav className="flex items-center gap-6">

          <NavLink
            to="/dashboard"
            className={({ isActive }) =>
              `rounded-lg px-5 py-2 text-sm font-medium transition-all duration-200 ${
                isActive
                  ? "bg-black text-white"
                  : "text-slate-600 hover:bg-slate-100 hover:text-black"
              }`
            }
          >
            Dashboard
          </NavLink>



        </nav>

      </div>
    </header>
  );
}

export default Navbar;