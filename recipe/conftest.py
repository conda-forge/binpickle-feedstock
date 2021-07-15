import hypothesis

hypothesis.settings.register_profile('package', deadline=1000)
hypothesis.settings.load_profile('package')