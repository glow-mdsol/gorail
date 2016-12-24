# -*- coding: utf-8 -*-

"""
Contains the handlers for the Study Data
-> expected use case starts with the clinical study data (eg SAS Datasets)
"""
__author__ = 'glow'

from neo4j.v1 import GraphDatabase, basic_auth


class StudyDataDriver(object):

    def __init__(self, host, username="neo4j", password="neo4j"):
        _driver = GraphDatabase.driver("bolt://%s" % host,
                                       auth=basic_auth(user=username, password=password))
        self.session = _driver.session()

    def get_or_create_study(self, study_id):
        result = self.session.run("MATCH (a:Study) WHERE a.study_id = '{study_id}'", dict(study_id=study_id))
        if not result:
            self.session.run("CREATE (a:Study {study_id: '{study_id}'}", dict(study_id=study_id))
            result = self.session.run("MATCH (a:Study) WHERE a.study_id = '{study_id}'", dict(study_id=study_id))
        return result

    def get_or_create_subject(self, study_id, subject):
        result = self.session.run("MATCH (a:StudyParticipant) WHERE a.subject_id = '{subject_id}'",
                                  dict(subject_id=subject.get("subject_id")))
        if not result:
            study = self.get_or_create_study(study_id=study_id)
            self.session.run("MATCH (s:Study) WHERE s.study_id = '{study_id}'; "
                             "CREATE (a:StudyParticipant {subject_id: '{subject_id}'} -[:ParticipatedIn]->(s)",
                             dict(study_id=study_id, subject_id=subject.get("subject_id")))
            result = self.session.run("MATCH (a:StudyParticipant) WHERE a.subject_id = '{subject_id}'",
                                      dict(subject_id=subject.get("subject_id")))
        return result

    def get_or_create_value_domain(self, value_domain):
        """
        Create a new value domain
        :param value_domain:
        :return:
        """
        pass

    def get_or_create_permissible_value(self, value_domain, permissible_value):
        """
        Create a Permissible Value, with a link to a value domain
        :param value_domain: metadata around value domain
        :param permissible_value: instance value for a permissible domain
        :return:
        """
        cl = self.get_or_create_value_domain(value_domain=value_domain)
        pass

    def get_or_create_subject_visit(self, study_id, subject_id, subject_visit):
        """
        Get or Create a Subject Visit
        :param study_id: Name of the Study
        :param subject_id: Name of the Subject
        :param subject_visit: Data about the visit
        """
        pass

    def __del__(self):
        self.session.close()
