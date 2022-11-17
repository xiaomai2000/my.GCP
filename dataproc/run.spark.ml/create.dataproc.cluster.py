import sys
from google.cloud import dataproc_v1 as dataproc

def create_cluster(project_id, region, cluster_name):
    cluster_client = dataproc.ClusterControllerClient(
            client_options={"api_endpoint": f"{region}-dataproc.googleapis.com:443"}
    )

    cluster = {
            "project_id": project_id,
            "cluster_name": cluster_name,
            "config": {
                "master_config": {"num_instances": 1, "machine_type_uri": "n1-standard-2", "disk_config":{"boot_disk_size_gb":100}},
                "worker_config": {"num_instances": 2, "machine_type_uri": "n1-standard-2"},
                },
            }

    operation = cluster_client.create_cluster(
            request = {"project_id": project_id, "region": region, "cluster": cluster}
    )
    result = operation.result()

    print(f"Cluster created successfully: {result.cluster_name}")



if __name__ == "__main__":
    if len(sys.argv) < 4:
        sys.exit("Python create_cluster.py project_id region cluster_name")

    project_id = sys.argv[1]
    region = sys.argv[2]
    cluster_name = sys.argv[3]
    create_cluster(project_id, region, cluster_name)




