class data_wrangling():
    def Manhattan_select(self, df):
        CH = (df['zip_code'] == 10026) | (df['zip_code'] == 10027) | (df['zip_code'] == 10030) | (
                    df['zip_code'] == 10037) | (df['zip_code'] == 10039)
        CC = (df['zip_code'] == 10001) | (df['zip_code'] == 10011) | (df['zip_code'] == 10018) | (
                    df['zip_code'] == 10019) | (df['zip_code'] == 10020) | (df['zip_code'] == 10036)
        EH = (df['zip_code'] == 10029) | (df['zip_code'] == 10035)
        GPMH = (df['zip_code'] == 10010) | (df['zip_code'] == 10016) | (df['zip_code'] == 10017) | (
                    df['zip_code'] == 10022)
        GVS = (df['zip_code'] == 10012) | (df['zip_code'] == 10013) | (df['zip_code'] == 10014)
        LM = (df['zip_code'] == 10004) | (df['zip_code'] == 10005) | (df['zip_code'] == 10006) | (
                    df['zip_code'] == 10007) | (df['zip_code'] == 10038) | (df['zip_code'] == 10280)
        LE = (df['zip_code'] == 10002) | (df['zip_code'] == 10003) | (df['zip_code'] == 10009)
        UE = (df['zip_code'] == 10021) | (df['zip_code'] == 10028) | (df['zip_code'] == 10044) | (
                    df['zip_code'] == 10065) | (df['zip_code'] == 10075) | (df['zip_code'] == 10128)
        UW = (df['zip_code'] == 10023) | (df['zip_code'] == 10024) | (df['zip_code'] == 10025)
        IWH = (df['zip_code'] == 10031) | (df['zip_code'] == 10032) | (df['zip_code'] == 10033) | (
                    df['zip_code'] == 10034) | (df['zip_code'] == 10040)
        df_MAN = df.loc[CH | CC | EH | GPMH | GVS | LM | LE | UE | UW | IWH]
        df_MAN = self.feature_engineer(df_MAN)

        return df_MAN

    def Queens_select(self, df):
        NQ = (df['zip_code'] == 11361) | (df['zip_code'] == 11362) | (df['zip_code'] == 11363) | (
                    df['zip_code'] == 11364)
        NQ1 = (df['zip_code'] == 11354) | (df['zip_code'] == 11355) | (df['zip_code'] == 11356) | (
                    df['zip_code'] == 11357) | (df['zip_code'] == 11358) | (df['zip_code'] == 11359) | (
                          df['zip_code'] == 11360)
        CQ = (df['zip_code'] == 11365) | (df['zip_code'] == 11366) | (df['zip_code'] == 11367)
        J = (df['zip_code'] == 11412) | (df['zip_code'] == 11423) | (df['zip_code'] == 11432) | (
                    df['zip_code'] == 11433) | (df['zip_code'] == 11434) | (df['zip_code'] == 11435) | (
                        df['zip_code'] == 11436)
        NQ2 = (df['zip_code'] == 11101) | (df['zip_code'] == 11102) | (df['zip_code'] == 11103) | (
                    df['zip_code'] == 11104) | (df['zip_code'] == 11105) | (df['zip_code'] == 11106)
        WCQ = (df['zip_code'] == 11374) | (df['zip_code'] == 11375) | (df['zip_code'] == 11379) | (
                    df['zip_code'] == 11385)
        R = (df['zip_code'] == 11691) | (df['zip_code'] == 11692) | (df['zip_code'] == 11693) | (
                    df['zip_code'] == 11694) | (df['zip_code'] == 11695) | (df['zip_code'] == 11697)
        SQ = (df['zip_code'] == 11004) | (df['zip_code'] == 11005) | (df['zip_code'] == 11411) | (
                    df['zip_code'] == 11413) | (df['zip_code'] == 11422) | (df['zip_code'] == 11426) | (
                         df['zip_code'] == 11427) | (df['zip_code'] == 11428) | (df['zip_code'] == 11429)
        SQ1 = (df['zip_code'] == 11414) | (df['zip_code'] == 11415) | (df['zip_code'] == 11416) | (
                    df['zip_code'] == 11417) | (df['zip_code'] == 11418) | (df['zip_code'] == 11419) | (
                          df['zip_code'] == 11420) | (df['zip_code'] == 11421)
        WQ = (df['zip_code'] == 11368) | (df['zip_code'] == 11369) | (df['zip_code'] == 11370) | (
                    df['zip_code'] == 11372) | (df['zip_code'] == 11373) | (df['zip_code'] == 11377) | (
                         df['zip_code'] == 11378)
        df_QUE = df.loc[NQ | NQ1 | CQ | J | NQ2 | WCQ | R | SQ | SQ1 | WQ]
        df_QUE = self.feature_engineer(df_QUE)

        return df_QUE

    def Brooklyn_select(self, df):
        CB = (df['zip_code'] == 11212) | (df['zip_code'] == 11213) | (df['zip_code'] == 11216) | (
                    df['zip_code'] == 11233) | (df['zip_code'] == 11238)
        SB = (df['zip_code'] == 11209) | (df['zip_code'] == 11214) | (df['zip_code'] == 11228)
        BP = (df['zip_code'] == 11204) | (df['zip_code'] == 11218) | (df['zip_code'] == 11219) | (
                    df['zip_code'] == 11230)
        CF = (df['zip_code'] == 11234) | (df['zip_code'] == 11236) | (df['zip_code'] == 11239)
        SB1 = (df['zip_code'] == 11223) | (df['zip_code'] == 11224) | (df['zip_code'] == 11229) | (
                    df['zip_code'] == 11235)
        NB = (df['zip_code'] == 11201) | (df['zip_code'] == 11205) | (df['zip_code'] == 11215) | (
                    df['zip_code'] == 11217) | (df['zip_code'] == 11231)
        F = (df['zip_code'] == 11203) | (df['zip_code'] == 11210) | (df['zip_code'] == 11225) | (
                    df['zip_code'] == 11226)
        ENYNL = (df['zip_code'] == 11207) | (df['zip_code'] == 11208)
        G = (df['zip_code'] == 11211) | (df['zip_code'] == 11222)
        SP = (df['zip_code'] == 11220) | (df['zip_code'] == 11232)
        BW = (df['zip_code'] == 11206) | (df['zip_code'] == 11221) | (df['zip_code'] == 11237)
        df_BRO = df.loc[CB | SB | BP | CF | SB1 | NB | F | ENYNL | G | SP | BW]
        df_BRO = self.feature_engineer(df_BRO)

        return df_BRO

    def Staten_island_select(self, df):
        PR = (df['zip_code'] == 10302) | (df['zip_code'] == 10303) | (df['zip_code'] == 10310)
        SS = (df['zip_code'] == 10306) | (df['zip_code'] == 10307) | (df['zip_code'] == 10308) | (
                    df['zip_code'] == 10309) | (df['zip_code'] == 10312)
        SSG = (df['zip_code'] == 10301) | (df['zip_code'] == 10304) | (df['zip_code'] == 10305)
        MI = (df['zip_code'] == 10314)
        df_STAN = df.loc[PR | SS | SSG | MI]
        df_STAN = self.feature_engineer(df_STAN)

        return df_STAN

    def Bronx_select(self, df):
        CB = (df['zip_code'] == 10453) | (df['zip_code'] == 10457) | (df['zip_code'] == 10460)
        BPF = (df['zip_code'] == 10458) | (df['zip_code'] == 10467) | (df['zip_code'] == 10468)
        HBM = (df['zip_code'] == 10451) | (df['zip_code'] == 10452) | (df['zip_code'] == 10456)
        HPMH = (df['zip_code'] == 10454) | (df['zip_code'] == 10455) | (df['zip_code'] == 10459) | (
                    df['zip_code'] == 10474)
        KR = (df['zip_code'] == 10463) | (df['zip_code'] == 10471)
        NB = (df['zip_code'] == 10466) | (df['zip_code'] == 10469) | (df['zip_code'] == 10470) | (
                    df['zip_code'] == 10475)
        SB = (df['zip_code'] == 10461) | (df['zip_code'] == 10462) | (df['zip_code'] == 10464) | (
                    df['zip_code'] == 10465) | (df['zip_code'] == 10472) | (df['zip_code'] == 10473)

        df_BRONX = df.loc[CB | BPF | HBM | HPMH | KR | NB | SB]
        df_BRONX = self.feature_engineer(df_BRONX)

        return df_BRONX

    def preprocess(self, df):
        from uszipcode import SearchEngine
        search = SearchEngine(simple_zipcode=True)
        df = df.astype({"latitude": float, "longitude": float})
        df.loc[df['zip_code'].isnull() & df['latitude'] & df['longitude'], 'zip_code'] = df[
            df['zip_code'].isnull() & df['latitude'] & df['longitude']].apply(self.get_zipcode, axis=1)
        df = df.dropna(axis=0, subset=['zip_code'])
        df = df.astype({"zip_code": float})
        return df

    def feature_engineer(self, df):
        import pandas as pd
        import numpy as np
        df['crash_date'] = pd.to_datetime(df['crash_date'])
        crash_num_per_day = df['crash_date'].value_counts()
        df = pd.DataFrame(crash_num_per_day)
        df = df.reset_index()
        df.rename(columns={'index': 'CRASH DATE', 'crash_date': 'CRASH NUMBER'}, inplace=True)
        df = df.sort_values('CRASH DATE', ascending=True)
        df['const'] = 1
        df.set_index('CRASH DATE', inplace=True)
        df['Julian'] = df.index.to_julian_date()
        df['sin(week)'] = np.sin(df['Julian'] / 7 * 2 * np.pi)
        df['cos(week)'] = np.cos(df['Julian'] / 7 * 2 * np.pi)
        df['sin(biweek)'] = np.sin(df['Julian'] / 3.5 * 2 * np.pi)
        df['cos(biweek)'] = np.cos(df['Julian'] / 3.5 * 2 * np.pi)
        df['sin(biyear)'] = np.sin(df['Julian'] / 180 * 2 * np.pi)
        df['cos(biyear)'] = np.cos(df['Julian'] / 180 * 2 * np.pi)
        df['sin(year)'] = np.sin(df['Julian'] / 360 * 2 * np.pi)
        df['cos(year)'] = np.cos(df['Julian'] / 360 * 2 * np.pi)

        return df

    def get_zipcode(self, df):
        from uszipcode import SearchEngine
        search = SearchEngine(simple_zipcode=True)
        zipcode = search.by_coordinates(df['latitude'], df['longitude'])
        if not zipcode:
            return None
        else:
            return zipcode[0].values()[0] 