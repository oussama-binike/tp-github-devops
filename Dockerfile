FROM maven:3.9.6-eclipse-temurin-17 AS build

WORKDIR /app

# Copier les fichiers Maven
COPY pom.xml .
COPY src ./src
RUN mvn clean package -DskipTests

# ==========================
# Stage 2 : Run
# ==========================
FROM eclipse-temurin:17-jre

WORKDIR /app

# Copier le JAR généré depuis le stage build
COPY --from=build /app/target/*.jar app.jar

EXPOSE 8070

ENTRYPOINT ["java", "-jar", "app.jar"]