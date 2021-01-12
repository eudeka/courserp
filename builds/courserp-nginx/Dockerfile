FROM bitnami/node:12-prod

COPY install_app.sh /install_app

RUN /install_app courserp https://github.com/eudeka/courserp version-13-beta

FROM frappe/frappe-nginx:version-13-beta

COPY --from=0 /home/frappe/frappe-bench/sites/ /var/www/html/
COPY --from=0 /rsync /rsync
RUN echo -n "\ncourserp" >> /var/www/html/apps.txt

VOLUME [ "/assets" ]

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]