from mycroft import MycroftSkill, intent_file_handler


class TrainJobs(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('jobs.train.intent')
    def handle_jobs_train(self, message):
        self.speak_dialog('jobs.train')


def create_skill():
    return TrainJobs()

