# Use Node.js image as base
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application files to the container
COPY . .

# Build the React app for production
RUN npm run build

# Set environment variable to serve the app on port 80
ENV PORT=80

# Expose port 80 to the outside world
EXPOSE 80

# Command to run the React app
CMD ["npm", "start"]
