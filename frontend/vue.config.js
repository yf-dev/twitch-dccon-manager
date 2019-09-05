process.env.VUE_APP_API_PROTOCOL = process.env.API_PROTOCOL;
process.env.VUE_APP_API_HOSTNAME = process.env.API_HOSTNAME;

module.exports = {
  css: {
    loaderOptions: {
      sass: {
        includePaths: ['./node_modules'],
      },
    },
  },
};
