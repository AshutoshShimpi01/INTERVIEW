

Here are 30 concise interview questions and answers covering **CI/CD, Docker, and Kubernetes** suitable for a data engineer or cloud engineer role:

***

### CI/CD

1. **What is CI/CD?**  
Continuous Integration (CI) automates building and testing code. Continuous Deployment/Delivery (CD) automates code releases to production.

2. **Why is CI/CD important?**  
It helps catch bugs early, ensures faster deployments, and improves code quality.

3. **Name some popular CI/CD tools.**  
Jenkins, GitLab CI, GitHub Actions, CircleCI, Azure DevOps.[3][5]

4. **How do you trigger a CI pipeline?**  
Commonly triggered by a code push or pull request to the repository.

5. **What is a build artifact?**  
A compiled output from a build process (like a Docker image, JAR file).

6. **What does “pipeline as code” mean?**  
Defining CI/CD steps in configuration files, like Jenkinsfile or .gitlab-ci.yml.

7. **How do you run tests in CI/CD?**  
Include automated test steps in the pipeline (unit, integration tests).

8. **What is rollback in CD?**  
Reverting to a previous stable version when deployments fail.

9. **What is blue-green deployment?**  
Deploying new code alongside old, switching traffic only if the new version is healthy.

10. **How does version control relate to CI/CD?**  
CI/CD pipelines rely on version control (Git) for code changes and tracking.

***

### Docker

11. **What is Docker?**  
It’s an open-source platform to package applications into containers for easy deployment and scaling.[1][5][7]

12. **What is a Docker image vs. container?**  
Image: template for containers. Container: running instance of an image.[2]

13. **How do you build a Docker image?**  
Use a Dockerfile, and run `docker build`.

14. **How do you run a Docker container?**  
`docker run image_name`.

15. **What is Docker Compose?**  
A tool for managing multi-container apps with a YAML config file.

16. **What is Docker Hub?**  
A cloud registry for sharing Docker images.

17. **How do you expose a port in Docker?**  
Use `-p <host_port>:<container_port>` in `docker run`.

18. **How do containers differ from virtual machines?**  
Containers share host OS kernel, VMs emulate separate OS—containers are lighter..[7][1]

19. **What is a volume in Docker?**  
Persistent storage that survives container restarts.

20. **How do you view running containers?**  
`docker ps`

21. **How can you clean up unused containers and images?**  
`docker system prune` or `docker rm`, `docker rmi`.

22. **How can you inspect logs for a container?**  
`docker logs container_id`

***

### Kubernetes

23. **What is Kubernetes?**  
An open-source platform for managing, scaling, and automating containerized applications.

24. **What is a pod?**  
The smallest deployment unit in Kubernetes; runs one or more containers.

25. **What is a deployment in Kubernetes?**  
Manages replicas and updates of pods.

26. **How does Kubernetes provide service discovery?**  
Through built-in Service resources which map to pod endpoints.

27. **What is a node in Kubernetes?**  
A machine (VM or physical) where pods run.

28. **What is a namespace in Kubernetes?**  
Logical partition for resources; good for multi-team or multi-environment separation.

29. **How do you scale applications in Kubernetes?**  
Increase/decrease replica count with deployment spec.

30. **What is a config map and secret in Kubernetes?**  
Config Map: stores configuration; Secret: stores sensitive data (passwords, tokens).

***

Let me know if you want more depth or scenario-based answers for any question!

[1](https://www.interviewbit.com/docker-interview-questions/)
[2](https://www.datacamp.com/blog/docker-interview-questions)
[3](https://www.turing.com/interview-questions/docker)
[4](https://www.simplilearn.com/tutorials/docker-tutorial/docker-interview-questions)
[5](https://www.geeksforgeeks.org/devops/docker-interview-questions/)
[6](https://www.youtube.com/watch?v=HHcgzhfuaWc)
[7](https://www.edureka.co/blog/interview-questions/docker-interview-questions/)
[8](https://www.vinsys.com/blog/docker-interview-questions-and-answers)
[9](https://razorops.com/blog/top-50-docker-interview-question-and-answers/)
