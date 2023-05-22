# WriteSQLInsertsPy

Head txt

DECLARE @rowCount int = (select count(*) from powerapps.SLAEscalationMatrix)
select @rowCount;
IF (@rowCount = 0)
BEGIN
END
