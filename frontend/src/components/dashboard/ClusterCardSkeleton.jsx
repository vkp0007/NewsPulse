import Skeleton from "../common/Skeleton";

function ClusterCardSkeleton() {

    return (

        <div className="rounded-2xl border border-slate-200 bg-white p-6">

            <div className="flex items-start justify-between">

                <Skeleton className="h-7 w-3/4" />

                <Skeleton className="h-7 w-16 rounded-full" />

            </div>

            <Skeleton className="mt-6 h-4 w-full" />
            <Skeleton className="mt-3 h-4 w-5/6" />
            <Skeleton className="mt-3 h-4 w-4/6" />

            <div className="mt-8 flex gap-2">

                <Skeleton className="h-8 w-16 rounded-full" />
                <Skeleton className="h-8 w-20 rounded-full" />
                <Skeleton className="h-8 w-24 rounded-full" />

            </div>

            <Skeleton className="mt-8 h-4 w-32" />

        </div>

    );

}

export default ClusterCardSkeleton;