import sentry_sdk

sentry_sdk.init(
    dsn="https://827d6d3cb69988b24e9543f26e4a70e5@o4506122431692800.ingest.sentry.io/4506125339656192",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

division_by_zero = 1 / 0