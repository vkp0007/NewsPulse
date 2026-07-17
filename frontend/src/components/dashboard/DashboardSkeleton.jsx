import DashboardStatsSkeleton from "./DashboardStatsSkeleton";
import ClusterCardSkeleton from "./ClusterCardSkeleton";
import Skeleton from "../common/Skeleton";

function DashboardSkeleton() {

    return (

        <div className="space-y-10">

            {/* Header */}

            <section>

                <Skeleton className="h-4 w-40" />

                <Skeleton className="mt-4 h-14 w-80" />

                <Skeleton className="mt-6 h-5 w-2/3" />

            </section>

            {/* Stats */}

            <DashboardStatsSkeleton />

            {/* Section */}

            <div>

                <Skeleton className="h-8 w-56" />

                <Skeleton className="mt-3 h-5 w-72" />

            </div>

            {/* Cards */}

            <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-3">

                {[1, 2, 3, 4, 5, 6].map((item) => (

                    <ClusterCardSkeleton key={item} />

                ))}

            </div>

        </div>

    );

}

export default DashboardSkeleton;