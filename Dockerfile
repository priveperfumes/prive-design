FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
COPY DESIGN.md /usr/share/nginx/html/DESIGN.md
EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]