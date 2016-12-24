# -*- coding: utf-8 -*-
import os
import xport

__author__ = 'glow'


class SubjectLoader(object):
    """
    Loads the SV and DM records
    """

    def __init__(self, location):
        self.location = location

    def _load(self, dsname):
        content = []
        if not os.path.exists(os.path.join(self.location, dsname)):
            print("No dataset, nothing to do")
        else:
            content = xport.load(open(os.path.join(self.location, dsname), 'rb'))
        return content

    def load_subject_visits(self):
        """
        Load SV data
        :return:
        """
        content = self._load('sv.xpt')
        study_id = None
        subject_visits = {}
        for line in content:
            if study_id is None:
                study_id = line.STUDYID
            subject = subject_visits.setdefault(line.USUBJID, {})
            subject[line.VISITNUM] = dict(name=line.VISIT,
                                          start=line.SVSTDTC,
                                          end=line.SVENDTC)
        return study_id, subject_visits

    def load_subject_ae(self):
        """
        Load AE Data
        :return:
        """
        content = self._load('ae.xpt')
        study_id = None
        subject_visits = {}
        for line in content:
            if study_id is None:
                study_id = line.STUDYID
            subject = subject_visits.setdefault(line.USUBJID, {})
            subject[line.VISITNUM] = dict(name=line.VISIT,
                                          start=line.AESTDTC,
                                          end=line.AEENDTC,
                                          )
        return study_id, subject_visits

    def load_subject_demographics(self):
        content = self._load('dm.xpt')
        subjects = {}
        for line in content:
            subjects[line.USUBJID] = dict(subject_id=line.USUBJID,
                                          start=line.RFSTDTC,
                                          end=line.RFENDTC,
                                          gender=line.SEX,
                                          dob=line.BRTHDTC,
                                          race=line.RACE,
                                          ethnicity=line.ETHNIC,
                                          arm=line.ARMCD,
                                          country=line.COUNTRY)
        return subjects
